$(document).ready(function () {

    $('#add').click(function () {
        // console.log(22)
        var $number = $('#number')
        var $max = $number.attr('max')
        var $badge = $('#badge')
        if ($number.val() <= parseInt($max)) {
            console.log(44)
            $.ajax({
                url: '/api/add_to_basket',
                type: "POST",
                data: {
                    quantity: $number.val(), name_product: $('.name_product').html(), price: $('.price').html(),
                    _id: $('[name="product"]').attr('id')
                },
                success: function (resp) {
                    $number.attr('max', $max - $number.val())
                    $badge.html(parseInt($badge.html())+1)
                    $badge.show()
                    alert(resp['result'])
                }
            })


        }

    })


})