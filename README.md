![Logo](https://media.discordapp.net/attachments/989648770138513448/1045430527034929152/Loki_icon.png?width=400&height=400)
## LOKI - manipulation is key.
"Ransomware is unique among cybercrime because in order for the attack to be successful, it requires the victim to become a willing accomplice even after the fact."

## Features: 🔥
- Self-protection. ✔
- Encryption. ✔
- Decryption. ✔
- Key generation. ✔
- Ransomware* ✔
- Discord webhooks. ✔
- Lokified scp file sending. ❌
- Vault. 🚧
- Share. ❌

## Installation & Deployment: 💾
To deploy this project open WSL or Terminal, then copy/paste:

```cd /home/$USER && git clone https://github.com/ItsJustShepherd/Loki && cd LOKI && sudo pip install -r requirements.txt && python3 loki.py```

You can add this to an alias with the following:

```alias loki="python3 /home/$USER/Loki/loki.py"```

## Variables: ⚙
To run this project, you can either use arguements (shown below) or run it with `python3 loki.py` to get a CLI-menu.

`-encrypt` ✔
This is used for encrypting a directory and it's sub-directories contents.

`-decrypt` ✔
This is used for decrypting a directory and it's sub-directories contents.

`-keygen` ✔
This is used for backing up the current ```loki.key``` file or for generating a new one, don't loose it!

`-hook` ✔
This is for sending files to yourself via Discord Webooks (dhooks), at present and by default it'll only send the ```loki.key``` file along with a message to Discord Webooks (dhooks).

`-vault` 🚧
Vault can be used to secure copy files from remote servers, or locally, into Loki's vault system which has a unique and seperate key as a whole to ```loki.key``` - it's strongly suggested you only add or remove files from the vault through Loki as to avoid accident file destruction.

`-share` ❌
Send files over the Linux scp command, but it gets packaged up in a nice lokified zip first.

## Acknowledgements: ❗
### Supporters;
 For quite some time I've hidden away from releasing any projects, and worked in private under an alt because I was getting tired of people abusing my kindness, my openness for wanting to bring about a better state of open-source in terms of nit-picking commentation in code, pushing only when I'm certain something works with pre-existing code and wouldn't impeed on others development, and if not for the persistant pushing, support and dedication from some tireless friends both digital and physical who helped me overcome my anxieties, depression and woes or worries - I never would of made a 'come back' project, let alone Loki.
  So for that, I thank you all.
### Notice;
 *Loki exists not for the ransomware potential, it was developed with the knowledge that modern day movements such as [reporters without borders](https://rsf.org/en) are frequently challenged in the fact they're censored and screened constantly when wanting to release press from blacked out countries or regions, the rising potential for [government media blackouts](https://en.wikipedia.org/wiki/Media_blackout) is ever present and Orwellian control is on the north-bound increase.  Organizations like AVAAZ, Extinction Rebellion and Anon-cells, even press writers, reporters and private-individuals are under scrutiny and observation.
 
 Whether they're being pried on or not.  Loki is a form of resistance against state, government and corpo control of our data.  How safe is 'cloud' storage when in reality it's simply someone else's computer?  Can you trust Google, Microsoft, Apple, your own Government - well why take that extra risk when you can Loki vault your files with encryption before uploading, use it to encrypt/decrypt your Linux home directory on login/logoff or your SoHo servers along with LUKS.  Taking control of your data, your freedoms, the ability to share documents, resources and files without peer-oversight with Loki - manipulation is key and security starts at home.  If you're in the EU, know your rights and freedoms [here](https://ec.europa.eu/info/aid-development-cooperation-fundamental-rights/your-rights-eu_en) begin to fight back, the law is there for us too if you know how to use it.

## FAQ: 📣
#### Can I send my friend an encrypted file for them to decrypt?

Yes, one of the biggest reasons Loki was developed was for privacy purposes - so long as the other computer/user has the loki.key file that was used to encrypt the directory/file/zip, then yes they can decrypt it on their side using Loki too.  I already plan on streamlining this whole process with a ```-share``` argument in future updates. 

#### I encrypted my files and generated a new key, what can I do?

Unfortunately, not much, unless you've made a backup.  By default when using ```-keygen``` Loki will prompt you asking if you'd like to back up your previous key, if you selected yes just do the following:
```mv loki.key loki.key.alt && cp loki.key.bk loki.key && mv loki.key.alt loki.key.bk```this will swap your backup and current keys around. Due to the nature of encryption/decryption it might not even be possible to recover any files you've encrypted if your key is lost, or damaged. However the [Cryptex](https://github.com/SSGorg/Cryptex) dev-team is working with me on a reverse enginering of Loki already, so one day we can add in a key recovery service type function!

In future there will be a ```-swapout``` argument which simplifies this.

#### Doesn't it look suspicious if your encrypting your data?

Not at all, and why should it?

In the EU everyone has the right to respect for his or her private and family life, home and communications - this includes how you go about securing that.
This right is enshrined in article 7 of the Charter of Fundamental Rights. Not to forget the protection of personal data concerning him or her inclusive of access to data which has been collected concerning him or her, and the right to have it rectified.
This right is enshrined in article 8 of the Charter of Fundamental Rights.

Don't take it as legal advice, because it isn't, but it sounds to me that we have a right to protect our data as we see fit. So do just that...
 developing on this you also have to consider that corpos (corporations, business entities, essentially non-gov) also have access to the files you upload to their services such as 'drives', 'email attachments' and so forth - who knows if they're keeping copies?
  Well we certainly don't know and it isn't worth the risk, is it?

Please, if you're in the EU take a moment to read over your rights [here](https://ec.europa.eu/info/aid-development-cooperation-fundamental-rights/your-rights-eu_en) and enact them whenever and however you can.

#### What file types does it encrypt and in what format?

Fernet Encryption is used at present and is a Python standard for encryption/authentication that guarantees a message (for example: "Hello, this is an encryption") is encrypted securely enough that it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.

At present Loki currently affects all formats, but you can modify Loki to ignore certain extentions by editing the code directly.

## Unlicense: 📃
[Unlicense.org](https://unlicense.org/) - TL;DR; "Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means." in last addition no forks or developments coming from Loki can be licensed any other way than Unlicense themselves.
 With all that said-and-done, any attribution to the original Loki would be appreciated, of course.