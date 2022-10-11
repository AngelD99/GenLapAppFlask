/* Preload website */
jQuery(document).ready(function($){
    $(".mw-preload").fadeOut('slow');
  });


  $('#owl-1').owlCarousel({
    loop: true,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:false,
    dots:true,
    nav:false,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    margin:10,
    responsive:{
             0:{
                 items:1,
                 },
                 600:{
                    items:2,
                },
                 1000:{
                    items:3
              }
       },
    autoHeight: true,
    onInitialized: setOwlStageHeight,
    onResized: setOwlStageHeight,
    onTranslated: setOwlStageHeight
});

function setOwlStageHeight(event) {
    var maxHeight = 0;
    $('#clientes.owl-item.active').each(function () {
        var thisHeight = parseInt( $(this).height() );
        var maxHeight2 = (maxHeight>=thisHeight?maxHeight:thisHeight);
   
    $('#clientes.owl-carousel').css('height', maxHeight2 );
    $('#clientes.owl-stage-outer').css('height', maxHeight2 );
  });
};

$('#owl-2').owlCarousel({
  loop: true,
  autoplay:true,
  autoplayTimeout:3000,
  // autoplayHoverPause:true,
  dots:false,
  navText: ['<i class="fal fa-angle-left" aria-hidden="true"></i>', '<i class="fal fa-angle-right" aria-hidden="true"></i>'],
  margin:10,
  responsive:{
           0:{
               items:1,
               nav:false
               },
               600:{
                   items:3,
                   nav:false
              },
               1000:{
                   nav:true,
                   items:3
            }
     },
  autoHeight: true,
  onInitialized: setOwlStageHeight,
  onResized: setOwlStageHeight,
  onTranslated: setOwlStageHeight
});

function setOwlStageHeight(event) {
  var maxHeight = 0;
  $('#clientes.owl-item.active').each(function () {
      var thisHeight = parseInt( $(this).height() );
      var maxHeight2 = (maxHeight>=thisHeight?maxHeight:thisHeight);
 
  $('#clientes.owl-carousel').css('height', maxHeight2 );
  $('#clientes.owl-stage-outer').css('height', maxHeight2 );
});
};


$('#owl-3').owlCarousel({
  loop: true,
  autoplay:true,
  autoplayTimeout:3000,
  // autoplayHoverPause:true,
  nav:false,
  navText: ['<i class="fas fa-arrow-circle-left" aria-hidden="true"></i>', '<i class="fas fa-arrow-circle-right" aria-hidden="true"></i>'],
  margin:10,
  responsive:{
           0:{
              items:1,
              dots:false,
              },
               600:{
              items:2,
              dots:false,
              },
              1000:{
              dots:true,
              items:2
            }
     },
  autoHeight: true,
  onInitialized: setOwlStageHeight,
  onResized: setOwlStageHeight,
  onTranslated: setOwlStageHeight
});

function setOwlStageHeight(event) {
  var maxHeight = 0;
  $('#clientes.owl-item.active').each(function () {
      var thisHeight = parseInt( $(this).height() );
      var maxHeight2 = (maxHeight>=thisHeight?maxHeight:thisHeight);
 
  $('#clientes.owl-carousel').css('height', maxHeight2 );
  $('#clientes.owl-stage-outer').css('height', maxHeight2 );
});
};

$('#owl-4').owlCarousel({
  loop: true,
  autoplay:true,
  autoplayTimeout:3000,
  // autoplayHoverPause:true,
  nav:false,
  dots:true,
  navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
  margin:10,
  responsive:{
           0:{
               items:1
               },
               600:{
                   items:3
              },
               1000:{
                   items:3
            }
     },
  autoHeight: true,
  onInitialized: setOwlStageHeight,
  onResized: setOwlStageHeight,
  onTranslated: setOwlStageHeight
});

function setOwlStageHeight(event) {
  var maxHeight = 0;
  $('#clientes.owl-item.active').each(function () {
      var thisHeight = parseInt( $(this).height() );
      var maxHeight2 = (maxHeight>=thisHeight?maxHeight:thisHeight);
 
  $('#clientes.owl-carousel').css('height', maxHeight2 );
  $('#clientes.owl-stage-outer').css('height', maxHeight2 );
});
};

//Formbox
$('#myBtn01').on('click', function() {
  $.fancybox.open( $('.mw_contact-01'), {
  type:'inline',
  });
});

$('#myBtn02').on('click', function() {
  $.fancybox.open( $('.mw_contact-02'), {
  type:'inline',
  });
});

$('#myBtn03').on('click', function() {
  $.fancybox.open( $('.mw_contact-04'), {
  type:'inline',
  });
});

//Date picker
$(function() {
  $('.input-group').datepicker({
    clearBtn: true,
    language: "es"
  });
});