$(function () {
    'use strict'

    let cartas_flag = 0;

    $("#cartas").hide();
    $("#apuestaCarta").hide();

    $( "#noCartas" ).click(function() {

        $("#cartas").hide();
        $("#apuestaCarta").hide();

        cartas_flag = 0;

    });

    $( "#venderCartas" ).click(function() {

        $("#cartas").show();
        $("#apuestaCarta").show();

        cartas_flag = 1;

    });


    function checkKeno(element) {

        return element > 0 && element <= 80;

    }

    function removeLastValue(keno) {
        
        let keno_array = keno.split(' ');

        keno_array.pop();

        return keno_array.join(' ');
    }

    function isDuplicated(keno) {

        let elements = keno.split(' ').map(Number);
        
        let elements_tmp = elements.sort();

        for (let i = 0; i < elements_tmp.length - 1; i++) {
            
            if (elements_tmp[i + 1] == elements_tmp[i]) {

                return true;

            }   
        }

        return false;
    }

    function validateKeno(keno) {

        let elements = keno.split(' ').map(Number);

        if (elements.length == 10)
            return true;
        else 
            return false;
    }

    $('#keno').keypress(function(event){

        let keycode = (event.keyCode ? event.keyCode : event.which);

        // if enter is pressed
        if(keycode == '13') {

            let keno = $(this).val();
    
            let elements = keno.split(' ').map(Number);
            
            //  check the max count
            if (elements.length <= 10 ) {

                // check the validation
                if (elements.every(checkKeno)) {
                    
                    // check duplication
                    if (!isDuplicated(keno)) {
                        
                        $('.apuestas_ball_div').empty();

                        $.each(elements, function(index, value){

                            $('.apuestas_ball_div').append(
                                '<a class="apuestas_ball"><img src="../static/pv/img/Pelotas/Bola' + value + '.png" height="50" width="50"></a>'
                            );

                        });

                    } else {

                        alert ('You inputted duplicated value. Please input again.');

                        $('#keno').val(removeLastValue(keno));

                    }
                    
                    
                } else {

                    alert ('please input the correct number between 1 and 80.')
                    
                }

            } else {

                alert ('You have inputted 10 values.');

                // delete last character from keno (string)
                let keno = $(this).val();

                $('#keno').val(removeLastValue(keno));

            }

            return false;

        }
    });


    $( "#imprimir" ).click(function() {

        let keno = $('#keno').val();
        let keno_valor = 0;

        let cartas_valor = 0;
        let cartas_alta_baja = '';
        let cartas_color = '';

        cartas_valor = $( '#apuestaCarta' ).val();
        

        $( ".valor-header a" ).each(function( index ) {

            if ($( this ).hasClass('active'))
                keno_valor = $( this ).text();
        });

        // keno valor
        $( "#cartas a" ).each(function( index ) {

            if ($( this ).hasClass('active')) {

                cartas_alta_baja = $(this).attr('data-alta-baja');
                cartas_color = $(this).attr('data-color');

            }
    
        });

        if (!validateKeno(keno)) {

            alert ('Please input the Keno Numeros.');
            return false;
        }

        if (cartas_flag == 1) {
            
            if (cartas_valor == '') {

                alert ('Please select the valor of cartas');
                return false;
            }

            if (cartas_alta_baja == '' && cartas_color == '') {

                alert ('Please select the cartas card');
                return false;

            }
        }

        
        

        return false;
    });

    


});
