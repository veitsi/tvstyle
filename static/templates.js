var templates = {
    'c11': {
        items: 2
    },
    'hearts': {
        items: 5
    },
    'elegant': {
        items: 6
    },
    'styled': {
        items: 7
    },
    'ink': {
        items: 5
    }

};
function loadTemplate(id) {
    document.querySelector('#canvas')
        .appendChild(document.importNode(
            document.querySelector('link[rel="import"]').import.querySelector('#' + id).content, true));
    var i = 1;
    for (i; i <= templates[id].items; i++) {
        console.log("#" + i);
        $(".item-"+i).droppable({drop: droppedIn});

        //$("#" + i).attr('src', links[i]);
        //$("#" + i).droppable({drop: droppedIn});
    }

}


//        var link = document.querySelector('link[rel="import"]');
//        var template = document.querySelector('link[rel="import"]').import.querySelector('#ink');
//        var clone = document.importNode(template.content, true);

