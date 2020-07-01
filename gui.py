import tkinter as tk
from tkCanvasGraph import CanvasFrame, Vertex, Edge
from kruskall import graph, kruskal
import random
# vertex lists
vv = []

# edges list
edges = []

"""convert edge format of kruskall algorithm to edge format of kcanvasgraph libray"""


def edge_format_converter(e):
    for edge in edges:
        if e[0] == edge.origin.label and e[1] is edge.end.label and e[2] is edge.label:
            return edge


"""return diffrence of two list (list1 - list2)"""


def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

"""convert vertex object to str for kruskall file """
def make_vertex():
    vlist = []
    for v in vv:
        vlist.append(v.label)
    return vlist

"""convert edge object to str tubple for kruskall file """

def make_edge():
    elist = []
    for e in edges:
        v1 = e.origin.label
        v2 = e.end.label
        w = e.label
        elist.append((v1, v2, w))
    return elist


def start_kruskal():
    v = make_vertex()
    e = make_edge()
    g = graph(v, e) #make graph
    print("edges ",e)
    print("vertexes: ",v)
    print(g.getv())
    a = kruskal(g)
    final_edges = [] # kruskal result's edges
    for i in a:
        final_edges.append(edge_format_converter(i))

    deleted_edges = diff(edges, final_edges)
    for i in deleted_edges:
        if i is not None:
            frame.canvas.delete_element(i)

"""make edge from ui """
def create_edge():
    v1 = fnode_ent.get()
    v2 = lnode_ent.get()
    w = edge_weight_ent.get()
    edge = Edge(frame.canvas, vv[int(v1)], vv[(int(v2))], label="{}".format(w))
    edges.append(edge)
    frame.canvas.add_edge(edge)
    fnode_ent.delete(0, tk.END)
    lnode_ent.delete(0, tk.END)
    edge_weight_ent.delete(0, tk.END)
    print("edge created!!! ", v1, v2, "  weight  :", w)

"""generate vertexes of graph with user input """
def create_vertex():
    n = int(vertex_ent.get())
    for i in range(n):
        vv.append(Vertex(frame.canvas, label="vertex{}".format(i)))
        frame.canvas.add_vertex(vv[i])
    vertex_ent.destroy()
    vertex_btn.destroy()


"""create initial vertex (only random graph)"""
def create_vertexx(n):
    for i in range(n):
        vv.append(Vertex(frame.canvas, label="vertex{}".format(i)))
        frame.canvas.add_vertex(vv[i])

    # delete vertex generator after generating vertexes
    vertex_ent.destroy()
    vertex_btn.destroy()

"""m"""
def create_random_graph():
    n = random.randint(1,10)
    create_vertexx(n)
    e = random.randint(0,(n*(n-1))/2)
    if e > 20 :
        e = random.randint(2,10)
    for i in range(e):
        v1 = random.randint(0, n - 1)
        v2 = random.randint(0, n - 1)

        # end and origin is identical
        if v1 == v2 :
            continue
        w = random.randint(1, 20)
        edge = Edge(frame.canvas, vv[v1], vv[v2], label="{}".format(w))
        edges.append(edge)
        frame.canvas.add_edge(edge)

    random_btn.destroy()

# ui
root = tk.Tk()

menu_frame = tk.Frame(master=root, width=50)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)
frame = CanvasFrame(root)
can = CanvasFrame(root, bg="blue")
frame.pack(fill="both", expand=True, side=tk.LEFT)

# menu_entry :


vertex_btn = tk.Button(master=menu_frame, command=create_vertex, text="number of vertexes",bg = "#1fac02")
vertex_btn.pack()
empty_frm =tk.Frame(master=menu_frame,height = 20)
empty_frm.pack()
vertex_ent = tk.Entry(master=menu_frame)
vertex_ent.pack()

empty_frm1 =tk.Frame(master=menu_frame,height = 20)
empty_frm1.pack()

edge_btn = tk.Button(master=menu_frame, command=create_edge, text="new edge",bg = "#ffaca2",width=15)
edge_btn.pack()

fnode_frm = tk.Frame(master=menu_frame)
fnode_lbl = tk.Label(master=fnode_frm, text="from")
fnode_lbl.pack()
fnode_ent = tk.Entry(master=fnode_frm)
fnode_ent.insert(0, "from")
fnode_ent.pack()
fnode_frm.pack()


lnode_frm = tk.Frame(master=menu_frame)
lnode_lbl = tk.Label(master=lnode_frm, text="  to      ")
lnode_lbl.pack()
lnode_ent = tk.Entry(master=lnode_frm)
lnode_ent.insert(0, "to")
lnode_ent.pack()
lnode_frm.pack()


edge_weight_frm = tk.Frame(master=menu_frame)
edge_weight_lbl = tk.Label(master=edge_weight_frm, text="weight")
edge_weight_ent = tk.Entry(master=edge_weight_frm)
edge_weight_lbl.pack()
edge_weight_ent.insert(0, "weight")
edge_weight_ent.pack()
edge_weight_frm.pack()



# kruskall button
kruskal_btn = tk.Button(master=menu_frame, command=start_kruskal, text="kruskal",bg = "#ffac02",width =15)
kruskal_btn.pack()
#
# random graph button
random_btn = tk.Button(master=menu_frame, command=create_random_graph, text="random graph",bg = "#aa2aaf",width =15)
random_btn.pack()
#


root.mainloop()


