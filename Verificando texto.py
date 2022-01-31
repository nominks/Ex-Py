import emoji

c = str(input('Digite a cidade em que você nasceu:')).replace(' ', '')
if c[:5].upper() == 'SANTO':
    print(emoji.emojize('✅✅✅ Opa! Essa cidade está correta. ✅✅✅'))
else:
    print(emoji.emojize('💀💀💀 Calma lá! Você não nasceu nesta cidade, programa encerrando. 💀💀💀'))
