def iou(box1, box2):
    """Implement the intersection over union (IoU) between box1 and box2
    
    Arguments:
    box1 -- first box, list object with coordinates (x1, y1, x2, y2)
    box2 -- second box, list object with coordinates (x1, y1, x2, y2)
    """

    # Calculate the (y1, x1, y2, x2) coordinates of the intersection of box1 and box2. Calculate its Area.
    ### START CODE HERE ### (≈ 5 lines)
    xi1 = np.maximum(box1[0],box2[0])
    yi1 = np.maximum(box1[1],box2[1])
    xi2 = np.minimum(box1[2],box2[2])
    yi2 = np.minimum(box1[3],box2[3])
    inter_area = (yi1 - yi2)*(xi1 - xi2)
    ### END CODE HERE ###    

    # Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)
    ### START CODE HERE ### (≈ 3 lines)
    box1_area = (box1[3] - box1[1])*(box1[2]-box1[0])
    box2_area = (box2[3] - box2[1])*(box2[2]-box2[0])
    union_area = box1_area + box2_area - inter_area
    ### END CODE HERE ###
    
    # compute the IoU
    ### START CODE HERE ### (≈ 1 line)
    iou = inter_area/union_area
    ### END CODE HERE ###

    return iou
