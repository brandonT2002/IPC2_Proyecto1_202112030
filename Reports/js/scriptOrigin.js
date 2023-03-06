d3.select('#original').graphviz().scale(.6).height(document.getElementById('original').clientWidth).renderDot(`digraph html {
    matrizInicial [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    <tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">0</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">1</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">2</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">3</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">4</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">5</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">6</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">7</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">8</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">9</font></td><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">10</font></td></tr> <tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">1</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">2</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">3</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">4</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#CC4125" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">5</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">6</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="#E06666" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">7</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#FFD966" width="60" height="60" border="1"></td>
    <td BGCOLOR="#F6B26B" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">8</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#F6B26B" width="60" height="60" border="1"></td>
    <td BGCOLOR="#FFD966" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    </tr><tr><td BGCOLOR="white" width="60" height="60" border="0"><font point-size="30">9</font></td><td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="white" width="60" height="60" border="1"></td>
    <td BGCOLOR="#F6B26B" width="60" height="60" border="1"></td>
    <td BGCOLOR="#FFD966" width="60" height="60" border="1"></td>
    </tr></TABLE>>];
    organismos [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="5" CELLPADDING="20">
    <tr>
    <td BGCOLOR="#CC4125" width="60" height="60"><font point-size="20">A - 1</font></td>
    </tr>
    <tr>
    <td BGCOLOR="#E06666" width="60" height="60"><font point-size="20">B - 2</font></td>
    </tr>
    <tr>
    <td BGCOLOR="#F6B26B" width="60" height="60"><font point-size="20">C - 3</font></td>
    </tr>
    <tr>
    <td BGCOLOR="#FFD966" width="60" height="60"><font point-size="20">D - 4</font></td>
    </tr>
    </TABLE>>];
    }`)