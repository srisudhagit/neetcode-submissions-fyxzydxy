class MinStack {
    Stack<Integer> numStack, minStack;

    public MinStack() {
        numStack = new Stack<>();
        minStack = new Stack<>();   
    }
    
    public void push(int val) {
        numStack.push(val);
        int num = Math.min(val,(minStack.isEmpty()? val : minStack.peek()));
        minStack.push(num);
    }
    
    public void pop() {
        numStack.pop();
        minStack.pop();
    }
    
    public int top() {
       return numStack.peek();
    }
    
    public int getMin() {
       return minStack.peek();
    }
}
