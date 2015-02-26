$(function(){
    $(".wronghide").delay(1500).slideUp();
    $(".wrong").click(function(){
       $(".wronghide").slideToggle();
    }); 

   
   
    $(".action").click(function(){
        var person = $(this).parent();
        var ismale = person.find(".action").hasClass("male");
        var name = person.find(".name").text();

        var content = person.clone();
        content.removeClass("person").addClass("popup_person");
      
        if(ismale)
        {
            content.append($("#male_text").clone().children());
        }
        else
        {
            content.append($("#female_text").clone().children());
        }
        
      
        content.filter(function(){
            var html = $(this).html();
            var emailPattern = /[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/;
            var matched_str = $(this).html().match(emailPattern);
            if(matched_str){
                $(this).html(html.replace(emailPattern,"<a href='mailto:"+matched_str+"'>"+matched_str+"</a>"));
                return $(this)
            }
        });

        var content_outer = $('<div></div>');
        content_outer.append(content);
      
        $.fancybox({
			'orig'			: person,
			'padding'		: 10,
			'content'       : content_outer.html().replace(/MEPNAME/g, name),
			'transitionIn'	: 'elastic',
			'transitionOut'	: 'elastic'
		});
        
        piwikTracker.trackGoal(1);
        
        
        
        
   });
   
   
   
   
   
});
