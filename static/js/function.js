$(".add-to-cart").on("click", function(){
    let quantity = $(".product-quantity").val()
    let product_name = $(".product-name").val()
    let product_price = $(".product-price").text()
    let product_id = $(".product-id").val()
    let this_val = $(this)

    console.log("Quantity:", quantity);
    console.log("product_name:", product_name);
    console.log("product_price:", product_price);
    console.log("product_id:", product_id);
    console.log("this_val:", this_val);

    $.ajax({
      url: '/add-to-cart',
      data: {
          'id': product_id,
          'qty': quantity,
          'title': product_name,
          'price': product_price,
      },
      dataType: 'json',
      beforeSend: function(){
          console.log("Adding Product to Cart....");
      },
      success: function(response){
          this_val.html("Item Added To Cart")
          console.log("Added Product to Cart!");
          $(".cart-item-count").text(response.totalcartitems)
      }

    })

})

$(document).ready(function(){
    $(".filter-checkbox").on("click", function(){
        console.log("checkbox has been clicked....");
        let filter_object = {}

        $(".filter-checkbox").each(function(){
              let filter_value = $(this).val()
              let filter_key = $(this).data("filter")

              filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key +']:checked')).map(function(element){
                    return element.value
              })
        })
        console.log("filter object is:", filter_object);
        $.ajax({
          url: '/filter-products',
          data: filter_object,
          dataType: 'json',
          beforeSend: function(){
            console.log("sending data....");
          },
          success: function(response){
            console.log("data sent....");
            console.log(response);
            $("#filter_product").html(response.data)
           }
        })
    })
})