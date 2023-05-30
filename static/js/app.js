function increaseQuantity(quantityField){
    document.getElementById(quantityField).value++
}

function decreaseQuantity(quantityField){
    value = document.getElementById(quantityField).value
    if(value > 1){
        document.getElementById(quantityField).value--
    }
}