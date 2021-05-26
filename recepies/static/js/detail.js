$('#delete').click((event)=>{
    $.ajax({
        type: "POST",
        url: event.target.getAttribute("uri"),
        success: () => window.location.replace("/")
    });
});

