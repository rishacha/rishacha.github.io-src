{%- extends 'basic.tpl' -%}

{% block header %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
img {
    max-width:none
}
div.output_area img, div.output_area svg {
    max-width: none;
    height: auto;
}

div.output_subarea {
    overflow-x: auto;
    -webkit-box-flex: 1;
    -moz-box-flex: 1;
    box-flex: 1;
    flex: 1;
    max-width: none;
}

div.output_area img, div.output_area svg {
    max-width: none;
    background-color: hsl(0deg 30% 80%);
    height: auto;
}
.MathJax,.MathJax_Display {
    color: hsl(0deg 30% 80%) !important;
}
</style>
{%- endblock header %}