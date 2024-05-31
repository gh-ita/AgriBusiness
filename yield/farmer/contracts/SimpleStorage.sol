pragma solidity ^0.8.0;

contract Yield {
    // Mapping to store the products associated with an address
    mapping(address => string) public products;
    
    // Nested mapping to store the quantity of a product associated with an address
    mapping(address => mapping(string => uint)) public quantities;

    // Event emitted when a product is stored
    event ProductStored(address indexed user, string product, uint quantity);

    // Function to store the product and its quantity
    function store(string memory product, uint quantity) public {
        // Store the product for the sender's address
        products[msg.sender] = product;
        
        // Update the quantity of the product for the sender's address
        quantities[msg.sender][product] += quantity;

        // Emit an event
        emit ProductStored(msg.sender, product, quantity);
    }
}

