# coding: utf-8

import numpy, math, matplotlib

def calc_circumcircle(array_triangle_vertices):
    '''The input array of triangle vertices should have shape (N_triangles, 3, 2) and this function should use the vertex information to calculate and return numpy arrays containing the circumcenters and circumradii for the circumcircles of each triangle.'''
    def sum_squares_vertex(coordinates):
        square_coordinates = [coordinate**2 for coordinate in coordinates]
        sum_squares = sum(square_coordinates)
        return sum_squares
    def calc_sum_squares_each_vertex(vertex_1_coords,vertex_2_coords,vertex_3_coords):
        vertex_1_sum_squares = sum_squares_vertex(vertex_1_coords)
        vertex_2_sum_squares = sum_squares_vertex(vertex_2_coords)
        vertex_3_sum_squares = sum_squares_vertex(vertex_3_coords)
        return (vertex_1_sum_squares, vertex_2_sum_squares, vertex_3_sum_squares)
    list_circumcenters = [] #an ordered list of circumcenter coords
    list_circumradii = [] #a correspondingly ordered list of circumradii
    for triangle in array_triangle_vertices:
        vertex_1_sum_squares, vertex_2_sum_squares, vertex_3_sum_squares = calc_sum_squares_each_vertex(triangle[0,...],triangle[1,...],triangle[2,...])
        x_determinant = numpy.array([[vertex_1_sum_squares, triangle[0,1], 1],\
                                     [vertex_2_sum_squares, triangle[1,1], 1],\
                                     [vertex_3_sum_squares, triangle[2,1], 1]])
        y_determinant = numpy.array([[vertex_1_sum_squares, triangle[0,0], 1],\
                                     [vertex_2_sum_squares, triangle[1,0], 1],\
                                     [vertex_3_sum_squares, triangle[2,0], 1]])
        a_determinant = numpy.array([[triangle[0,0], triangle[0,1], 1],\
                                     [triangle[1,0], triangle[1,1], 1],\
                                     [triangle[2,0], triangle[2,1], 1]])
        c_determinant = numpy.array([[vertex_1_sum_squares,triangle[0,0],triangle[0,1]],\
                                     [vertex_2_sum_squares,triangle[1,0],triangle[1,1]],\
                                     [vertex_3_sum_squares,triangle[2,0],triangle[2,1]]])
        denominator = 2.0 * numpy.linalg.det(a_determinant)
        circumcenter_x_coordinate = numpy.linalg.det(x_determinant) / denominator
        circumcenter_y_coordinate = -1.0 * (numpy.linalg.det(y_determinant)/ denominator)
        #adjuting for the negative coefficient of c:
        circumradius = math.sqrt(numpy.linalg.det(x_determinant)**2 + numpy.linalg.det(y_determinant)**2 + (4 * numpy.linalg.det(a_determinant) * numpy.linalg.det(c_determinant))) / (2 * abs(numpy.linalg.det(a_determinant)))
        #append the values of interest to their respective lists:
        list_circumcenters.append([circumcenter_x_coordinate,circumcenter_y_coordinate])
        list_circumradii.append([circumradius])
    #return a tuple of numpy arrays:
    return (numpy.array(list_circumcenters),numpy.array(list_circumradii))
    
    #call the function to obtain the numpy arrays of circumcenters and circumradii:
    #array_circumcenters, array_circumradii = calc_circumcircle(triangle_vertex_coords)
    #array_circumcenters has shape (N_circles, 2)
    #array_circumradii has shape (N_circles, 1)

    #now plot the circumcircles on top of the Delaunay triangulation
    #start by plotting the circumcenters in red:
#    from matplotlib.collections import PatchCollection
#    patches = []
#    ax1.scatter(array_circumcenters[...,0],array_circumcenters[...,1],c='r',marker='o',alpha = 0.4, edgecolors = 'none')
#    #now plot the circles:
#    for circumcenter_coordinates, circumradius in zip(array_circumcenters,array_circumradii):
#        patches.append(matplotlib.patches.Circle((circumcenter_coordinates[0],circumcenter_coordinates[1]),circumradius[0],color='r',fill=False, alpha=0.4))
#    p = PatchCollection(patches, alpha=0.4,match_original = True)
#    ax1.add_collection(p)
#    fig4.savefig('voronoi_stage_7.png',dpi=300)
