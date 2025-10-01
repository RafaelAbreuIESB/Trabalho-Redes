# Network Traffic Monitor Dashboard

![Python](https://img.shields.io/badge/python-3.10+-blue.svg) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Scapy](https://img.shields.io/badge/scapy-orange) ![Chart.js](https://img.shields.io/badge/Chart.js-FF5A5F?style=for-the-badge&logo=chartdotjs&logoColor=white)

## Descrição

Este projeto é uma ferramenta de monitoramento de tráfego de rede em tempo real. Utilizando uma porta espelhada ou escutando diretamente uma interface de rede, o sistema captura pacotes e exibe o volume de tráfego de entrada e saída em um dashboard web dinâmico. A visualização agrupa os dados por cliente (endereço IP) e permite uma análise mais profunda (*drill down*) para inspecionar a quebra de tráfego por protocolo.

## Funcionalidades

- **Visualização em Tempo Real**: Gráficos de barra atualizados em janelas de 5 segundos.
- **Tráfego por Cliente**: Agrupamento do volume de dados (In/Out) por cada endereço IP de cliente.
- **Análise por Protocolo**: Funcionalidade de *drill down* que revela a distribuição do tráfego entre protocolos (TCP, UDP, ICMP, etc.) para um cliente selecionado.
- **Dashboard Interativo**: Interface web construída com Flask e Chart.js para uma experiência de usuário fluida.

---

## Arquitetura

O sistema opera em um fluxo de trabalho simples e eficaz:

1.  **`capture.py`**: Utiliza a biblioteca `scapy` para capturar os pacotes da interface de rede especificada.
2.  **`aggregator.py`**: Recebe os pacotes capturados, extrai as informações relevantes (IPs, protocolo, tamanho) e os agrega em janelas de tempo.
3.  **`app.py`**: Um servidor web Flask que expõe os dados agregados através de uma API REST (`/metrics`) e serve o dashboard principal.
4.  **`templates/index.html`**: O frontend da aplicação, que consome a API e renderiza os gráficos dinâmicos usando Chart.js.

```
[Interface de Rede] -> capture.py -> aggregator.py -> app.py (API) <- [Dashboard Web]
```

---

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o ambiente de monitoramento.

### Pré-requisitos

- Python 3.8+
- **Para usuários Windows**: É **obrigatório** ter o driver **Npcap** instalado. 
  - Baixe no site oficial: [npcap.org](https://npcap.org)
  - Durante a instalação, marque a opção **"Install Npcap in WinPcap API-compatible Mode"**.

### Passos de Instalação

1.  **Clone o repositório (ou use os arquivos locais):**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirement.txt
    ```

### Configuração

Antes de iniciar, configure o arquivo `config.py`:

- **`SERVER_IP`**: Defina o endereço IPv4 da máquina que você deseja monitorar.
- **`CAPTURE_INTERFACE`**: Defina o nome da interface de rede que será monitorada.

**Como encontrar o nome da interface (Windows):**

Execute o script `get_interfaces.py` para listar todas as interfaces que o Scapy reconhece:

```bash
python get_interfaces.py
```

O resultado mostrará uma tabela. Copie o nome exato da sua placa de rede (ex: `"Intel(R) Wi-Fi 6 AX201 160MHz"`) e cole no campo `CAPTURE_INTERFACE`.

---

## Como Executar e Testar

### 1. Iniciar o Monitor

Com o ambiente virtual ativado e a configuração pronta, inicie o servidor:

```bash
python app.py
```

Abra seu navegador e acesse o dashboard em: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### 2. Gerar Tráfego para Teste

O gráfico só mostrará dados quando houver tráfego para o `SERVER_IP` configurado.

**A. Teste Local (no mesmo PC):**

- Configure `config.py`:
  - `SERVER_IP = "127.0.0.1"`
  - `CAPTURE_INTERFACE = "Software Loopback Interface 1"`
- Inicie o `app.py`.
- Em **outro terminal**, inicie um servidor web simples:
  ```bash
  python -m http.server 8080
  ```
- Acesse `http://127.0.0.1:8080` no seu navegador. O tráfego aparecerá no dashboard.

**B. Teste com Múltiplas Máquinas:**

- Configure `config.py` com o IP e a interface da sua rede principal (ex: Wi-Fi).
- Inicie o `app.py`.
- Em outros dispositivos (PCs, celulares) na mesma rede, acesse serviços rodando na máquina servidora (ex: `http://[SERVER_IP]:8080`).
- Observe os IPs de cada dispositivo aparecerem no dashboard.

## Pilha Tecnológica

- **Backend**: Python, Flask, Scapy
- **Frontend**: HTML, JavaScript, Chart.js
