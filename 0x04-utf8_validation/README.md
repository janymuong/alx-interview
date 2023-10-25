# UTF-8 Validation

> **Note**  
> WHAT `utf-8` IS:  
>> `UTF-8` stands for "***Unicode Transformation Format 8-bit***". Is a widely used character encoding standard for representing text and symbols from the Unicode character set. `Unicode` is a character encoding system that aims to cover the characters and symbols of all the world's written languages, as well as many special symbols used in computing and other fields. UTF-8 is one of several encoding schemes used to represent Unicode characters. It solves for massive incompatibility related to character encodiong in computing.  

### Adoption
UTF-8 has become the dominant character encoding for text data on the internet and in many software applications. It is widely supported by various programming languages, operating systems, and web standards. Its flexibility, efficiency, and multilingual support have contributed to its widespread adoption in the digital world.

## Project Requirements/Specifications
> Write a method that determines if a given data set represents a valid UTF-8 encoding.

```bash
Prototype: `def validUTF8(data)`
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer  
```

```bash
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```


---
## APPENDIX: Characteristics of UTF-8

- **Variable-Length Encoding**: UTF-8 uses a variable-length encoding scheme, which means that it can represent characters using different numbers of bytes. Basic ASCII characters (characters commonly used in English and other Western languages) are represented using a single byte in UTF-8, which allows UTF-8 to be backward-compatible with ASCII. Characters from other scripts and symbols are represented using multiple bytes as needed.

- **Multilingual Support**: UTF-8 can represent characters from various languages, scripts, and writing systems, making it a versatile choice for handling multilingual text. It can represent characters from Latin, Greek, Cyrillic, Arabic, Chinese, Japanese, and many other scripts.

- **Compatibility**: Because of its backward compatibility with ASCII, UTF-8-encoded text can be read and processed by systems that support ASCII, which is a subset of UTF-8. This makes it easier to transition from ASCII to UTF-8.

- **Self-Synchronization**: UTF-8 is designed in such a way that it's self-synchronizing, meaning it is easy to locate character boundaries in a stream of bytes. This allows for efficient parsing and manipulation of UTF-8 text.

- **Wide Range**: UTF-8 can represent over a million distinct code points, which is more than enough to cover the vast majority of characters and symbols in common use.
