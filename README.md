# Keys of Steffen Prince (sprin) <steffen@sprin.io>

I use tools based on [the OpenPGP
standard](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP) and [the
X.509 standard](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP) to
do [encryption](https://en.wikipedia.org/wiki/Public-key_encryption) of private
messages and [signing](https://en.wikipedia.org/wiki/Digital_signature) of
documents, code, public messages.

## The Master Key

All my keys are signed by the following Master Signing Key:

```
pub   4096R/3006E021 2016-07-05
      Key fingerprint = D0A6 F47A 49D6 7A7D 0369  4BE0 A587 D405 3006 E021
uid                  Steffen Prince (Master Signing Key) <steffen@sprin.io>
```

You should verify the fingerprint of this master key using some other channel
than just this repo (e.g. my [Hacker News
account](https://news.ycombinator.com/user?id=sprin) or from
https://keys.sprin.io) as in case somebody was providing you with a falsified
repo, they would be sure to also feed you with a falsified master key.

* The key is attached here: [sprin-master-key.asc](/sprin-master-key.asc).

## sprin.io Code Signing Key

The following key is used to sign projects managed by sprin.io:

```
pub   4096R/C489978F 2016-07-08
      Key fingerprint = BDAD A52E 42FE 70F6 A3B6  66E6 6FFD 3241 C489 978F
uid                  Steffen Prince (sprin.io Code Signing Key) <steffen@sprin.io>

gpg> check
uid  Steffen Prince (sprin.io Code Signing Key) <steffen@sprin.io>
sig!3        C489978F 2016-07-08  [self-signature]
sig!         3006E021 2016-07-08  Steffen Prince (Master Signing Key) <steffen@s
```

* The key is attached here: [sprin-io-code-signing-key.asc](/sprin-io-code-signing-key.asc).

## Credits

Credits to [Qubes OS Project](https://www.qubes-os.org/) for a good example of
code-signing in action and the excellent "Split GPG" mechanism which
dramatically minimizes the risk of compromise of the signing mechanism:

* [On Digital Signatures and Key Verification](https://www.qubes-os.org/doc/verifying-signatures/)
* [Qubes Split GPG](https://www.qubes-os.org/doc/split-gpg/)


Credits to [Joanna Rutkowska](http://blog.invisiblethings.org/) of [Qubes
OS](https://www.qubes-os.org/) and [Invisible Things
Lab](http://invisiblethingslab.com/) for a nice template on how to self-publish
key information on which this repository is based:

* [My Keys (Rutkowska)](http://blog.invisiblethings.org/keys/)
* [rootkovska/rootkovska.github.io](https://github.com/rootkovska/rootkovska.github.io/)

## License/Copyrights

This repo is licensed under a [Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
