var templates = {
    'c11': {
        items: 1
    },
    'hearts': {
        items: 5
    },
    'elegant':{
        items:6
    },
    'ink':{
        items:5
    }

};
    function loadTemplate(id) {
        document.querySelector('#canvas')
                .appendChild(document.importNode(
                        document.querySelector('link[rel="import"]').import.querySelector('#' + id).content, true));
    }


    //        var link = document.querySelector('link[rel="import"]');
    //        var template = document.querySelector('link[rel="import"]').import.querySelector('#ink');
    //        var clone = document.importNode(template.content, true);

