# OpenSSL

## Instalation

### For Windows:
----------------

1. Go to https://slproweb.com/products/Win32OpenSSL.html and scroll down until the table "Download Win32/Win64 OpenSSL" appears.
2. Select and download EXE or MSI package for your architecture (x64 or x86) that DOESN'T have in the name "Light", these are recommended for developers.
3. Install the downloaded package and test the installation with a shell running:
```PowerShell
$> openssl version
OpenSSL 3.5.0 8 Apr 2025 (Library: OpenSSL 3.5.0 8 Apr 2025)
```

### For Linux and other OS
--------------------------

You can find it with the default package installer (apk, apt, yum, etcetera).

## Generate certificates

Use this command once you have restarted you machine:

```PowerShell
$> openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout privkey.pem -out fullchain.pem
```

**This command generates a self-signed SSL certificate**, which is often used for testing or local development. Here's what each part does:

1. openssl req → Calls the OpenSSL tool and specifies the request module (used to generate certificates).
2. -x509 → Instead of generating a Certificate Signing Request (CSR), this creates a self-signed certificate (X.509 format).
3. -nodes → Tells OpenSSL not to encrypt the private key with a passphrase (useful for automation).
4. -days 365 → Sets the certificate’s validity to 365 days (1 year).
5. -newkey rsa:2048 → Creates a new RSA key pair, with a 2048-bit key size (strong encryption).
6. -keyout privkey.pem → Saves the private key in privkey.pem.
7. -out fullchain.pem → Saves the generated certificate in fullchain.pem.

The result is:

1. privkey.pem → Your private key (decryption).
2. fullchain.pem → Your self-signed certificate, used by servers to enable HTTPS (encryption).

## Usage

The privkey.pem and fullchain.pem files are ready to use in your web server, for example NGINX, pointing to the paths after the basic SSL directives, listen to port 443 and redirecting with other server listening to port 80 redirecting the request address:

```conf
server {
    # Instead of 80 (http).
    listen 443 ssl;
    # In the professional setting here's your domain.
    server_name localhost;
    # SSL certificate path.
    ssl_certificate /etc/nginx/certs/fullchain.pem;
    # SSL key for certificate path.
    ssl_certificate_key /etc/nginx/certs/privkey.pem;

    # locations ...
}

# Setting other server directive listening to port 80 redirecting
# http addresses to our secure server.
server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}
```
