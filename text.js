// РЕЗУЛЬТАТЫ
    
  var
    countBedroomCh, // детская спальня
    countBedroom, // взрослая спальня
    countOffice, // офис
    countPlayroom, // игровая
    countLaundryroom, // постирочная;
    imgTitle = '', // изображение планировки;
    resultImgListSize = '4',
    urlShare = '';
  //обработка результатов
  function getResult () {
    //ДЕТСКАЯ
    //по одной на подростка
    var
      teenagerM = $(liveAddItem).find(valueInput + '[name="add"][value="s3"]'), //подросток М
      teenagerW = $(liveAddItem).find(valueInput + '[name="add"][value="d3"]'); //подросток Ж
    switch (true) {
      case (teenagerM.length + teenagerW.length >= 2):
        countBedroomCh = 2;
        break;
      case (teenagerM.length + teenagerW.length == 1):
        countBedroomCh = 1;
        break;
      default: 
        countBedroomCh = 0;
        break;
    }
    //ребенку и младенцу одного пола 0,5 комнаты
    var
      teenM = $(liveAddItem).find(valueInput + '[name="add"][value="s1"],' + valueInput + '[name="add"][value="s2"]'), //ребенок или младенец М
      teenW = $(liveAddItem).find(valueInput + '[name="add"][value="d1"],' + valueInput + '[name="add"][value="d2"]'); //ребенок или младенец Ж
    switch (true) {
      case (Math.round(teenM.length * 0.5) >= 2):
        countBedroomCh += 2;
        break;
      case (Math.round(teenM.length * 0.5) == 1):
        countBedroomCh += 1;
        break;
      default: 
        countBedroomCh += 0;
        break;
    }
    switch (true) {
      case (Math.round(teenW.length * 0.5) >= 2):
        countBedroomCh += 2;
        break;
      case (Math.round(teenW.length * 0.5) == 1):
        countBedroomCh += 1;
        break;
      default: 
        countBedroomCh += 0;
        break;
    }
    countBedroomCh = (countBedroomCh > 2) ? 2 : countBedroomCh;
    
    //СПАЛЬНЯ
    //спальня для партнера, и вторая, если больше 2 партнеров
    countBedroom = ($(liveAddItem + '.add-1').find(valueInput).length > 2) ? 1 : 0;
    //максимум на родителей 1 спальня
    countBedroom = ($(liveAddItem + '.add-2').find(valueInput).length && countBedroom < 2) ? countBedroom + 1 : countBedroom;
    //максимум для гостей 1 спальня
    countBedroom = ($(valueInput + '[name="guest"]:checked').val() == '1' && countBedroom < 2) ? countBedroom + 1 : countBedroom;
    
    //ОФИС
    //если выбрана работа на дому, то хотя бы 1 офис должен быть
    if (Number($(valueInput + '[name="work"]:checked').val()) > 0) {
      countOffice = 1;
      if (countBedroom + countBedroomCh <= 2 && Number($(valueInput + '[name="work"]:checked').val()) > 1) {
        countOffice = 2;
      }
    } else {
      countOffice = 0;
    }
    //убираем одну спальню
    countBedroom = (
      countOffice + countBedroomCh + countBedroom > 4 // сумма превышает 4
    ) ? 1 : countBedroom;
    
    //ИГРОВАЯ
    countPlayroom = (
      teenM.length + teenW.length >= 3 && // младенцев и детей больше 3 и более
      countOffice + countBedroomCh + countBedroom < 4 // сумма не превышает 4
    ) ? 1 : 0;
    
    //ПОСТИРОЧНАЯ
    countLaundryroom = ($(valueInput + '[name="wash"]:checked').val() == '1') ? 1 : 0;
    
    //обработка
    //...
    
    //выввод изображения
    imgTitle = 'img/' + countBedroomCh + '-' + countBedroom + '-' + countOffice + '-' + countPlayroom + '-' + countLaundryroom + '.jpg'; //Заголовок картинки
    $(resultShow + ' .result-img').html('<a data-fancybox href="' + imgTitle + '"><img src="' + imgTitle + '" alt=""></a>');
    
    //текст для клиента
    $('.text-client').html('<p></p>').find('p').load('img/text/' + countBedroomCh + '-' + countBedroom + '-' + countOffice + '-' + countPlayroom + '-' + countLaundryroom + '.txt');
    
    //для соц сетей
    imgCheckCreate();
    history.pushState('', document.title, window.location.pathname);
    urlShare = document.location.href +'result.php?t=' + countBedroomCh + '-' + countBedroom + '-' + countOffice + '-' + countPlayroom + '-' + countLaundryroom + '&imgs=' + imgChecked.join(';').replaceAll('img/', '').replaceAll('-thumb.jpg', '');

    urlShare = urlShare + '&page=' + encodeURIComponent(document.location.protocol + '//' + document.location.host + document.location.pathname);
    $('.ya-share2__item_service_vkontakte a').attr('href', 'https://vk.com/share.php?url=' + encodeURIComponent(urlShare));
    $('.ya-share2__item_service_facebook a').attr('href', 'https://www.facebook.com/sharer.php?src=sp&u=' + encodeURIComponent(urlShare));
    
    recordCheck();
    
  }
  getResult();