# coding: utf-8


def getCredentials():
    from  oauth2client import file
    import httplib2
    import ipywidgets as widgets
    print "Getting the credentials from file..."
    storage = file.Storage("oauth2.dat")
    credentials=storage.get()
    if credentials is None or credentials.invalid:
        print '❗'
        display(widgets.Valid(
            value=False,
            description='Credentials are ',
            disabled=False))
        display(widgets.HTML('go create a credential valid file here: <a target="_blank" href="cloud.google.auth.ipynb.ipynb">gcloud authorization notebook</a> and try again'))
    else:
        http_auth = credentials.authorize(httplib2.Http())
        print '✅ Ok'
        return credentials
