# We can do that, because website is a Python package
from Website import create_app

app = create_app()

#app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51KibcBIEGhScLw0TOq2y2T3bnR4yotYYYP2taPf2sJAThfnNgmVNVBCQGyNwQ6yYPk2gOP3vQIcPRocxS57mOj1w00nOnmcAsX'
#app.config['STRIPE_SECRET_KEY'] = 'sk_test_51KibcBIEGhScLw0TaKrfJit7i1dKKZS6QzqTuhxX0DIDrAOFbIfUpVCL30TDHmjwGag9YgWrJY3420wmNs89Apa200GFBp1qp6'

# Only if we run this file, not if we import this file are we going to run this app ?
if __name__ == '__main__':
    # Run Flask application/Run web server with command "debug=True"
    # Whenever we change our code, "debug=True" make sure that changes will be applied and webserver restart
    app.run(debug=True)