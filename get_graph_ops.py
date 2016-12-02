import tensorflow as tf
import sys
from tensorflow.python.platform import gfile
import model_analyzer
    
def get_graph_ops(filename):
    with tf.Session() as persisted_sess:
        print("load graph")
        with gfile.FastGFile(filename,'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            persisted_sess.graph.as_default()
            tf.import_graph_def(graph_def, name='')
        print("map variables")
        model_analyzer.analyze_ops(persisted_sess.graph, print_info=True)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "not enough parameters"
    else:
        get_graph_ops(sys.argv[1])
