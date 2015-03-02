import Foundation


class Solution {
    func maxProfit(prices: [Int]) -> Int {
        if prices.isEmpty {
            return 0
        }
        
        var minVal = prices[0], maxProfit = 0
        
        for price in prices {
            minVal = min(minVal, price)
            maxProfit = max(maxProfit, price-minVal)
        }
        
        return maxProfit
    }
}