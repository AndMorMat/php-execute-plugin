# Plugin para execução de arquivos PHP!

Plugin para sublime text que permite a execução de determinados blocos de código de maneira simplificada, ótimo para testar trechos de código diretamente no sublime text.

## Como funciona?

Ao selecionar um determinado bloco de código e executar o plugin, todo conteúdo dentro da seleção será copiado para outro arquivo, executado, e em seguida devolverá uma resposta que será inserida em forma de comentário ao final da seleção.

## Configurações
- Faça o download do arquivo e salve no diretório **User** dentro de **Packages** no sublime text, normalmente fica em */home/user/.config/sublime-text-3/Packages/User*
- Certifique-se de que a variável **php_path** está correta de acordo com o path do seu php, para confirmar digite */usr/bin/php -v* no terminal, você deve receber algumas informações referentes ao php instalado.
- Por último, defina um atalho para facilitar a execução do plugin, vá até **Preferences > Key Bindings**, no arquivo que abrir deve ser inserido o seguinte json:
	```
	[
	    { "keys": ["ctrl+shift+x"], "command": "execute"}
    ]
	```
## Como usar?

Selecione um bloco de codigo e precione o conjunto de teclas definidas no passo anterior, você verá o resultado da execução no final da seleção.
