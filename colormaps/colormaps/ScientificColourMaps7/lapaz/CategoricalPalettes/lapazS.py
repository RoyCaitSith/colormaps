# 
#         lapazS
#                   www.fabiocrameri.ch/colourmaps
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0.10352, 0.047787, 0.39353],      
           [0.99706, 0.94979, 0.95121],      
           [0.36082, 0.54989, 0.64017],      
           [0.17465, 0.32419, 0.57638],      
           [0.71002, 0.67743, 0.58847],      
           [0.52524, 0.6214, 0.60853],      
           [0.23932, 0.44474, 0.6286],      
           [0.13975, 0.19504, 0.49367],      
           [0.92163, 0.81176, 0.73224],      
           [0.44047, 0.59072, 0.62848],      
           [0.15554, 0.26061, 0.53818],      
           [0.20114, 0.3857, 0.60689],      
           [0.29243, 0.5002, 0.64018],      
           [0.61297, 0.64609, 0.58925],      
           [0.12359, 0.12648, 0.4447],      
           [0.82171, 0.73321, 0.63398],      
           [0.97687, 0.88777, 0.84724],      
           [0.2639, 0.47302, 0.63575],      
           [0.87606, 0.7712, 0.67832],      
           [0.76465, 0.70148, 0.60385],      
           [0.56854, 0.63393, 0.59796],      
           [0.16443, 0.29264, 0.55815],      
           [0.48252, 0.60725, 0.61913],      
           [0.13199, 0.16132, 0.46961],      
           [0.32486, 0.52597, 0.64168],      
           [0.39963, 0.57158, 0.63567],      
           [0.65966, 0.65978, 0.58495],      
           [0.14749, 0.22811, 0.51661],      
           [0.21855, 0.41558, 0.61892],      
           [0.11424, 0.089643, 0.41924],      
           [0.95503, 0.8512, 0.78985],      
           [0.1867, 0.35524, 0.59266],      
           [0.98876, 0.9175, 0.89625],      
           [0.6843, 0.66795, 0.58549],      
           [0.99344, 0.93379, 0.92382],      
           [0.15981, 0.2767, 0.54838],      
           [0.12791, 0.14407, 0.45724],      
           [0.25112, 0.459, 0.6325],      
           [0.37993, 0.56104, 0.63828],      
           [0.46139, 0.59931, 0.62402],      
           [0.96724, 0.86987, 0.8187],      
           [0.30818, 0.51329, 0.6413],      
           [0.20945, 0.40074, 0.61318],      
           [0.93989, 0.83179, 0.7609],      
           [0.16935, 0.30849, 0.5675],      
           [0.54681, 0.6278, 0.60314],      
           [0.90025, 0.79142, 0.70446],      
           [0.50382, 0.61458, 0.6139],      
           [0.15142, 0.2444, 0.52758],      
           [0.27766, 0.48677, 0.63831],      
           [0.1091, 0.06976, 0.4064],      
           [0.79313, 0.71641, 0.617],      
           [0.19361, 0.37054, 0.60004],      
           [0.18039, 0.33979, 0.58476],      
           [0.84963, 0.75162, 0.65458],      
           [0.34246, 0.53819, 0.6413],      
           [0.14363, 0.21165, 0.50529],      
           [0.11911, 0.10838, 0.43203],      
           [0.59056, 0.63995, 0.59324],      
           [0.13589, 0.17829, 0.48176],      
           [0.2285, 0.43025, 0.62407],      
           [0.41986, 0.58148, 0.63238],      
           [0.73684, 0.68853, 0.59444],      
           [0.63594, 0.6526, 0.58636],      
           [0.98265, 0.90074, 0.86839],      
           [0.98591, 0.90918, 0.88236],      
           [0.15765, 0.26868, 0.54333],      
           [0.69702, 0.67251, 0.58664],      
           [0.47194, 0.60335, 0.62161],      
           [0.94784, 0.84159, 0.77536],      
           [0.43012, 0.58619, 0.63051],      
           [0.6017, 0.64299, 0.59114],      
           [0.64769, 0.6561, 0.58545],      
           [0.22341, 0.42293, 0.62156],      
           [0.16684, 0.30057, 0.56289],      
           [0.11175, 0.079829, 0.41283],      
           [0.30018, 0.50679, 0.64083],      
           [0.51452, 0.61805, 0.61123],      
           [0.17748, 0.33201, 0.58063],      
           [0.35154, 0.5441, 0.64083],      
           [0.16211, 0.28467, 0.55332],      
           [0.19007, 0.3629, 0.59641],      
           [0.55765, 0.63089, 0.60051],      
           [0.93115, 0.82184, 0.7465],      
           [0.86308, 0.76129, 0.6661],      
           [0.14946, 0.23628, 0.52213],      
           [0.24508, 0.4519, 0.63064],      
           [0.91132, 0.80161, 0.7182],      
           [0.17192, 0.31636, 0.57199],      
           [0.99126, 0.92569, 0.91007],      
           [0.4509, 0.5951, 0.62631],      
           [0.13789, 0.18667, 0.48776],      
           [0.77884, 0.70871, 0.60994],      
           [0.49315, 0.61099, 0.61655],      
           [0.33356, 0.53214, 0.64158],      
           [0.15344, 0.25253, 0.53293],      
           [0.11673, 0.099126, 0.42564],      
           [0.18348, 0.34753, 0.58876],      
           [0.23377, 0.43753, 0.62641],      
           [0.57952, 0.63694, 0.59553]]      
      
lapazS_map = LinearSegmentedColormap.from_list('lapazS', cm_data)      
# For use of "viscm view"      
test_cm = lapazS_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(lapazS_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=lapazS_map)      
    plt.show()      
