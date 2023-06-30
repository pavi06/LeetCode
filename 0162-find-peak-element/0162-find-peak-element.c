int findPeakElement(int* nums, int numsSize){

    int start=0,end=numsSize-1,mid;
    while(start<end){
        mid=start+(end-start)/2;
        if(nums[mid]>nums[mid+1]){
            end=mid;
        }
        else{
            start=mid+1;
        }
    }
    return start;
}
