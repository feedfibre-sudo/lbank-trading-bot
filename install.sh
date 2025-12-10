#!/bin/bash

# Script d'installation automatique - LBank Trading Bot
# Auteur: feedfibre-sudo
# Usage: bash install.sh

echo "===================================="
echo " LBank Trading Bot - Installation"
echo "===================================="
echo ""

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}1. Mise \u00e0 jour du syst\u00e8me...${NC}"
sudo apt update
sudo apt upgrade -y

echo -e "\n${YELLOW}2. Installation de Python 3 et pip...${NC}"
sudo apt install python3 python3-pip git screen -y

echo -e "\n${YELLOW}3. Installation des d\u00e9pendances Python...${NC}"
pip3 install -r requirements.txt

echo -e "\n${YELLOW}4. Configuration des cl\u00e9s API...${NC}"
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}Fichier .env cr\u00e9\u00e9 !${NC}"
    echo -e "${RED}IMPORTANT: \u00c9ditez le fichier .env avec vos cl\u00e9s API:${NC}"
    echo "  nano .env"
    echo ""
    read -p "Appuyez sur Entr\u00e9e une fois les cl\u00e9s API configur\u00e9es..."
else
    echo -e "${GREEN}Fichier .env d\u00e9j\u00e0 existant.${NC}"
fi

echo -e "\n${YELLOW}5. Test du bot...${NC}"
echo "V\u00e9rification de l'installation..."
python3 -c "import requests; print('OK - Modules Python pr\u00eats!')" 2>/dev/null

if [ $? -eq 0 ]; then
    echo -e "${GREEN}\u2713 Installation r\u00e9ussie !${NC}"
else
    echo -e "${RED}\u2717 Erreur d'installation${NC}"
    exit 1
fi

echo -e "\n===================================="
echo -e "${GREEN}Installation termin\u00e9e !${NC}"
echo "===================================="
echo ""
echo "Pour lancer le bot:"
echo -e "  ${GREEN}python3 advanced_strategy.py${NC}"
echo ""
echo "Pour lancer en arri\u00e8re-plan 24/7:"
echo -e "  ${GREEN}screen -S lbank-bot${NC}"
echo -e "  ${GREEN}python3 advanced_strategy.py${NC}"
echo -e "  ${YELLOW}(Puis Ctrl+A puis D pour d\u00e9tacher)${NC}"
echo ""
echo "Pour se reconnecter:"
echo -e "  ${GREEN}screen -r lbank-bot${NC}"
echo ""
echo -e "${YELLOW}N'oubliez pas de configurer vos cl\u00e9s API dans .env !${NC}"
echo ""
