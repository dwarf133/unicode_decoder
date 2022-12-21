# Escapes-fucker
simple script to translate literal escape codes to Unicode

### Example:

* input: "\u041e\u041e\u041e \u0421\u041a \u00ab\u0421\u0431\u0435\u0440\u0431\u0430\u043d\u043a \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435\u00bb"
* output: "ООО СК «Сбербанк страхование»"

### Instalation:

```bash
git clone git@github.com:dwarf133/unicode_decoder.git
```
```bash
sudo chmod +x /your/folder/unicode_decoder/escapes-fucker.py 
```
Add to PATH (optional)
```bash
export PATH=/your/folder/unicode_decoder:$PATH
```

### Usage:

```bash
escapes-fucker.py path/to/text/file.txt
```
By this command the new file with decoded text will be created in path/to/text with name decoded_file.txt

Also it will warks with .json, .md and other

### ToDo:
* add string input mode
* make distributet packages 