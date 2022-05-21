from django.shortcuts import render

def index(request):
    color_names = ["noir", "rouge", "bleu", "vert" ]
    colors = []
    for i in range(50):
        val = f"{int(i * 255 / 50):02X}"
        noir = "#" + val * 3
        rouge = "#" + val + "0000"
        vert = "#" + "00" + val + "00"
        bleu = "#" + "0000" + val
        colors.append((noir, rouge, bleu, vert))
    return render(request, 'ex03/index.html', {'color_names': color_names, 'colors': colors})