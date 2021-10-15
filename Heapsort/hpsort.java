public static int[] heapSort(int[] nums) {
	//build the heap
	for(int i=nums.length-1;i>=0;i--)
		//merge the 2 sub-heaps below i, by bubbling nums[i] down to the correct location
		sink(nums,i,nums.length);
	//turn it into a sorted list
	for(int i=nums.length-1;i>0;i--){
		//remove the root, and put the last leaf at the root of the heap
		int tmp = nums[i];
		nums[i]=nums[0];
		nums[0] = tmp;
		//bubble the new root down to the correct location
		sink(nums,0,i);
	}
	return nums;
}
static void sink(int[] nums, int start, int end){
	int val = nums[start];
	int i = start, next = 2*i+1;
	while(next<end){
		if(next+1<end && nums[next+1]>nums[next])
			next++;
		if(nums[next]<=val)
			break;
		nums[i]=nums[next];
		i=next;
		next = 2*i+1; //2*i+1, 2*i+2 are the children of i
	}
	nums[i]=val;
}
Original code: O(nlogn) build heap

public static int[] heapSort(int[] nums) {
	//build the heap
	for(int i=1;i<nums.length;i++){
		int val = nums[i];
		int j=i, next = (j-1)/2; //(j-i)/2 is the index of this location's parent
		while(j>0 && nums[next]<val){
			nums[j]=nums[next];
			j=next;
			next = (j-1)/2;
		}
		nums[j]=val;
	}
	
	//turn it into a sorted list
	for(int i=nums.length-1;i>0;i--){
		int val = nums[i];
		nums[i]=nums[0];
		
		int j = 0, next = 1;
		while(next<i){
			if(next+1<i && nums[next+1]>nums[next])
				next++;
			if(nums[next]<=val)
				break;
			nums[j]=nums[next];
			j=next;
			next = 2*j+1; //2*j+1, 2*j+2 are the children of j
		}
		nums[j]=val;
	}
	return nums;
}
