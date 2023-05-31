// Increase product quantity in basket
function increaseQuantity(quantityField){
    document.getElementById(quantityField).value++
}
// Decrease product quantity in basket
// Ensure min value in basket is 1.
function decreaseQuantity(quantityField){
    value = document.getElementById(quantityField).value
    if(value > 1){
        document.getElementById(quantityField).value--
    }
}