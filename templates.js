var templates = {
    'c22': {
        items: 3, html: `
<div style="position:absolute; top:0; left: 0;
    border: black 1px solid">
    <img id="0" src="" width=50 height=80>
</div>
<div style="position:absolute; top:10px; left: 95px;
    border: black 1px solid">
    <img id="1" src="" width=80 height=80>
</div>
<div style="position: absolute;
    top: 100px; left: 100px; border: black 1px solid">
    <img id="2" src="" width=100 height=100>
</div>
`
    },
    'c3': {
        items: 3, html: `
<div style="position:absolute; top:0; left: 0;
    border: black 1px solid">
    <img id="0" src="" width=50 height=80>
</div>
<div style="position:absolute; top:50px; left: 45px;
    border: black 1px solid">
    <img id="1" src="" width=80 height=80>
</div>
<div style="position: absolute;
    top: 130px; left: 130px; border: black 1px solid">
    <img id="2" src="" width=100 height=100>
</div>
`
    }
};

function render_template(template, links) {
    console.log('processing ' + template);
    $("#canvas").empty();
    $('#canvas').append(templates[template].html);
    var i = 0;
    for (i; i < links.length; i++) {
        //console.log("#" + i);
        $("#" + i).attr('src', links[i])
    }
}

