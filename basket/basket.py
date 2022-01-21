

class Basket():
    """
    A base basket class, providing some default behaviours
    that can be inherited or overrided as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number': 1234567}
        self.basket = basket
