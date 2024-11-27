# ESP32-CAM com Análise de Imagens e Integração via flask

Este projeto utiliza o ESP32-CAM para capturar imagens automaticamente ou sob demanda, integrado a um servidor Flask que, processa as imagens em tempo real. O sistema foi projetado para operar 24/7 em um servidor Ubuntu, mas sem restrição de sistema. O objetivo é fornecer uma análise eficiente e flexível.

# Funcionalidades Principais:
## 1. Captura direto do ESP:
- Quando o botão físico do ESP32 é pressionado, a imagem é capturada e enviada via http para o flask, no servidor.

## 2. Análise de Imagem:
- O servidor Flask processa a imagem recebida, utilizando um modelo de aprendizado profundo para detecção de objetos.
- O resultado, contendo o objeto detectado com maior confiança, é retornado para o display I2C/serial.

## 3. Controle Remoto:
- A interface web do Flask oferece três opções para controle remoto do ESP32-CAM:
  - Capturar uma foto remotamente.
  - Visualizar a câmera ao vivo.
  - Enviar uma imagem para análise.
## 4. Personalização e Armazenamento.
- O usuário pode optar por salvar as imagens capturadas localmente no servidor.
- Todas as opções permitem realizar análises adicionais conforme desejado.

# Diferenciais:
- Operação contínua em um servidor dedicado Ubuntu, garantindo alta disponibilidade.
- Integração com hardware (ESP32-CAM e display I2C) para o feedback em tempo real.
- Interface intuitiva baseada em Flask, permitindo interação simples e funcional para usuários locais e remotos.
