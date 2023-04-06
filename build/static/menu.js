/*
    First of all we need to check, if our page is loaded.
    The problem is, that js could not load on our page.
    And it will not 
*/

if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    /*
    First of all, we will try code "Remove" buttons to actually remove from the page.
    We need to select this remove buttons and add an event to them
    To say when this is clicked, do smth
    */
    var removeCartItemsButtons = document.getElementsByClassName('btn-danger')
    console.log(removeCartItemsButtons)

    /*
        Loop through all of the different buttons inside of our cart
        https://www.youtube.com/watch?v=YeFzkC2awTM&t=137s 8:15
    */
    for(var i = 0; i < removeCartItemsButtons.length; i++) {
        var button = removeCartItemsButtons[i]
        button.addEventListener('click', removeCartItem)
    }

    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
    for(var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i]
        input.addEventListener('change', quantityChanged)
    }

    var addToCartButtons = document.getElementsByClassName('shop-item-button')
    for(var i = 0; i < addToCartButtons.length; i++) {
        var button = addToCartButtons[i]
        button.addEventListener('click', addToCartClicked)
    }

    document.getElementsByClassName('btn-purchase')[0].addEventListener('click', purchaseClicked)
}

function purchaseClicked() {
    var cartItems = document.getElementsByClassName('cart-items')[0]
    while(cartItems.hasChildNodes()) {
        cartItems.removeChild(cartItems.firstChild)
    }
    updateCartTotall()
}


function removeCartItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotall()
}


function quantityChanged(event) {
    /*
        Get quantity element
    */
    var input = event.target
    /*
        We want to check to see if the value inside of "quantity" input is a valid value
    */
    if(isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateCartTotall()

}


function addToCartClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
    var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    console.log(title, price, imageSrc)
    addItemToCart(title, price, imageSrc)
    updateCartTotall()
}

function addItemToCart(title, price, imageSrc){
    var cartRow = document.createElement('div')
    cartRow.classList.add('cart-row')
    var cartItems = document.getElementsByClassName('cart-items')[0]
    var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
    for(var i = 0; i< cartItemNames.length; i++) {
        if(cartItemNames[i].innerText == title) {
            alert('This item is already added to the cart')
            return 
        }
    }
    var cartRowContents = `
        <div class="cart-item cart-column">
            <img class="cart-item-image" src="${imageSrc}" width="100" height="100">
            <span class="cart-item-title">${title}</span>
        </div>
        <span class="cart-price cart-column">${price}</span>
        <div class="cart-quantity cart-column">
            <input class="cart-quantity-input" type="number" value="1">
            <button class="btn btn-danger" type="button">REMOVE</button>
        </div>`
    cartRow.innerHTML = cartRowContents
    cartItems.append(cartRow)
    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
}






/*
    We want to go through every single row in our cart
    We want to find the price and want to multiply that by the quantity
    And then add that together for every single one of our rows and display it in Total section
*/
function updateCartTotall() {
    /*
        First, we want all our cart rows.
        In "menu.html" all our car rows are inside of this "cart-items" and all have "cart-row" class
    */
   var cartItemContainer = document.getElementsByClassName('cart-items')[0]
   var cartRows = cartItemContainer.getElementsByClassName('cart-row')
   var total = 0
   for(var i = 0; i < cartRows.length; i++) {
       var cartRow = cartRows[i]
       var priceElement = cartRow.getElementsByClassName('cart-price')[0]
       var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
       var price = parseFloat(priceElement.innerText.replace('€', ''))
       var quantity = quantityElement.value
       total = total + (price*quantity)
   }
   total = Math.round(total * 100) / 100
   document.getElementsByClassName('cart-total-price')[0].innerText = '€' + total

}
 