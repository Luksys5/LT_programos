onmessage = function() {
    newArr = new Array();
    for(var i = 0; i < 100000; i++)
    {
        var rezult = 0;
        if( i % 2 == 0)
        {
            rezult *= 3;
            rezult += 2;
        }
        else
        {
            rezult /= 2;
            rezult -= 5;   
        }
        if(i > 0)
        {
            rezult += newArr[i - 1];
        }
        newArr.push(rezult);
    }
    self.postMessage(newArr);
}