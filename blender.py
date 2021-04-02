import math
import bpy  
from mathutils import Vector, Euler

# run
#filename = '/Users/allanmartins/Dropbox/prg_new/python/blender_script/blender.py'
#exec(compile(open(filename).read(), filename, 'exec'))


def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)

def getNormilizedFaceVertex(p1,p2,radius):
    sino = (p2[1]-p1[1])/sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    coso = (p2[0]-p1[0])/sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    p11 = (p1[0]+radius*sino, p1[1]-radius*coso, p1[2])
    p12 = (p1[0]-radius*sino, p1[1]+radius*coso, p1[2])
    p21 = (p2[0]+radius*sino, p2[1]-radius*coso, p1[2])
    p22 = (p2[0]-radius*sino, p2[1]+radius*coso, p1[2])
    return [p11,p12,p22,p21]



def addFakePaintLine(p1, p2, color,radius):
    #Define vertices and faces
    verts = getNormilizedFaceVertex(p1,p2,radius)
    faces = [(0,1,2,3)]
    # Define mesh and object variables
    me = bpy.data.meshes.new("O1.mesh")
    O1 = bpy.data.objects.new("O1", me)  
    #Set location and scene of object
    O1.location = (0,0,0)
    bpy.context.scene.objects.link(O1)
    #Create mesh
    me.from_pydata(verts,[],faces)
    me.update(calc_edges=True)
    paint = makeMaterial('Paint', color, (0.9,0.9,0.9), 1)
    setMaterial(O1, paint)
    return O1



def movePoints(points, dx):
    for p in points:
        p.location[0] += dx 
    nPoints = len(points)
    maxPoints = 390
    if (nPoints>maxPoints):
        for i in range(0,nPoints-maxPoints):
            # delete object
            bpy.ops.object.select_all(action='DESELECT')
            points[0].select = True
            bpy.ops.object.delete(use_global=False)
            # remove pointer
            points.remove(points[0])



pi = 3.141592653589793
L = 0.8

C1 = bpy.data.objects['circ1']
C2 = bpy.data.objects['circ2']
C3 = bpy.data.objects['circ3']
C4 = bpy.data.objects['circ4']
C5 = bpy.data.objects['circ5']
C6 = bpy.data.objects['circ6']
C7 = bpy.data.objects['circ7']
C8 = bpy.data.objects['circ8']
C9 = bpy.data.objects['circ9']
C10 = bpy.data.objects['circ10']
arm = bpy.data.objects['arm']
roll1 = bpy.data.objects['roll1']
roll2 = bpy.data.objects['roll2']
gear1 = bpy.data.objects['gear1']
gear2 = bpy.data.objects['gear2']
gear3 = bpy.data.objects['gear3']

#cam = bpy.data.objects['Camera']
#cam.location = (0,-8,13)
#cam.rotation_euler = Euler((pi/4,0,0),'XYZ')


# square
a1 = 1.909859316911758
a2 = 0.000000000150000
a3 = 0.636619772346361
a4 = 0.000000000075000
a5 = 0.381971863412909
a6 = 0.000000000050000
a7 = 0.272837045296494
a8 = 0.000000000037500
a9 = 0.212206590786836
a10 = 0.000000000030000

o1 = -0.000000000157080
o2 = 1.570796326794897
o3 = -0.000000000157080
o4 = 1.570796326794897
o5 = -0.000000000157079
o6 = 1.570796326794897
o7 = -0.000000000157079
o8 = 1.570796326794897
o9 = -0.000000000157079
o10 = 1.570796326794897

# stairs
o1 = 4.712388979991990
o2 = -0.000000001649336
o3 = 1.570796326402198
o4 = 4.712388980384690
o5 = 4.712388979991992
o6 = -0.000000001649333
o7 = 1.570796326402197
o8 = 4.712388980384690
o9 = 4.712388979991994
o10 = -0.000000001649347

a1 = 1.145915591497055
a2 = 0.572957795102175
a3 = 0.381971862957817
a4 = 0.000000000292500
a5 = 0.229183118317744
a6 = 0.190985931707091
a7 = 0.163702226985039
a8 = 0.000000000146250
a9 = 0.127323954622100
a10 = 0.114591559025019


C1.scale = (a1, a1, 1)
C2.scale = (a2, a2, 1)
C3.scale = (a3, a3, 1)
C4.scale = (a4, a4, 1)
C5.scale = (a5, a5, 1)
C6.scale = (a6, a6, 1)
C7.scale = (a7, a7, 1)
C8.scale = (a8, a8, 1)
C9.scale = (a9, a9, 1)
C10.scale = (a10, a10, 1)

board_texture = bpy.data.materials['board_co']
I = board_texture.node_tree.nodes['Image Texture'].image
T = board_texture.node_tree.nodes['Mapping']
img = I.pixels
W = I.size[0]
H = I.size[1]

points = list()
lastHead = 0

dx = 1.0/40.0

bpy.data.scenes[0].tool_settings.use_keyframe_insert_auto = True

for i in range(0,2*36):
    o = i*pi/180.0

    C1.rotation_euler = Euler((0,0,1*o+o1),'XYZ')
    C2.rotation_euler = Euler((0,0,2*o+o2),'XYZ')
    C3.rotation_euler = Euler((0,0,3*o+o3),'XYZ')
    C4.rotation_euler = Euler((0,0,4*o+o4),'XYZ')
    C5.rotation_euler = Euler((0,0,5*o+o5),'XYZ')
    C6.rotation_euler = Euler((0,0,6*o+o6),'XYZ')
    C7.rotation_euler = Euler((0,0,7*o+o7),'XYZ')
    C8.rotation_euler = Euler((0,0,8*o+o8),'XYZ')
    C9.rotation_euler = Euler((0,0,9*o+o9),'XYZ')
    C10.rotation_euler = Euler((0,0,10*o+o10),'XYZ')

    C2.location  = (C1.location[0]+a1*L*cos(1*o+o1),C1.location[1]+a1*L*sin(1*o+o1),C2.location[2])
    C3.location  = (C2.location[0]+a2*L*cos(2*o+o2),C2.location[1]+a2*L*sin(2*o+o2),C3.location[2])
    C4.location  = (C3.location[0]+a3*L*cos(3*o+o3),C3.location[1]+a3*L*sin(3*o+o3),C4.location[2])
    C5.location  = (C4.location[0]+a4*L*cos(4*o+o4),C4.location[1]+a4*L*sin(4*o+o4),C5.location[2])
    C6.location  = (C5.location[0]+a5*L*cos(5*o+o5),C5.location[1]+a5*L*sin(5*o+o5),C6.location[2])
    C7.location  = (C6.location[0]+a6*L*cos(6*o+o6),C6.location[1]+a6*L*sin(6*o+o6),C7.location[2])
    C8.location  = (C7.location[0]+a7*L*cos(7*o+o7),C7.location[1]+a7*L*sin(7*o+o7),C8.location[2])
    C9.location  = (C8.location[0]+a8*L*cos(8*o+o8),C8.location[1]+a8*L*sin(8*o+o8),C9.location[2])
    C10.location = (C9.location[0]+a9*L*cos(9*o+o9),C9.location[1]+a9*L*sin(9*o+o9),C10.location[2])

    headPos = C10.location[1] + L*a10*sin(10*o+o10)

    arm.location[1] = headPos


    x1 = 5.5
    x2 = 5.5-dx
    O1 = addFakePaintLine((x1,lastHead,3.4),(x2,headPos,3.4),(1,0,0),0.04)
    #print('%.4f %.4f to %.4f %.4f'%(x1,lastHead,x2,headPos))

    lastHead = headPos

    points.append(O1)

    movePoints(points,dx)
    T.translation = (0,i*dx/10,0)

    roll1.rotation_euler = Euler((0,o,0),'XYZ')
    roll2.rotation_euler = Euler((0,o,0),'XYZ')

    gear1.rotation_euler = Euler((0,0,o),'XYZ')
    gear2.rotation_euler = Euler((0,0,-o),'XYZ')
    gear3.rotation_euler = Euler((0,0,o),'XYZ')

    #cam.location = (12*sin(o)+6,-8*cos(o),13)
    #cam.rotation_euler = Euler((0.8*pi/4,0,o),'XYZ')

    #bpy.context.scene.render.filepath = '/Users/allanmartins/Desktop/Fourier Mech/f%04d.png'%i
    #bpy.ops.render.render(write_still=True)

    bpy.data.scenes[0].update()
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)








