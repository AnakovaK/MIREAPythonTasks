# Изображение граф игрового мира с помощью генерации кода на языке Dot – представления инструмента Graphviz.
'''digraph G {

  subgraph cluster_1 {
    node [style=filled];
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->8 ->9 -> 10;
    6->11->12->13->14
    6->15->16
    15->END
    label = "game";
    color=blue
  }
  start -> 1;
  2->1
  3->2
  4->3
  5->4
  6->5
  7->6
  8->7
  9->8
  9->10
  11->6
  12->11
  13->12
  14->13
  15->6
  16->15
  start [shape=Mdiamond];
}'''