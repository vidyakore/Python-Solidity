//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract first {

    uint256 public f;
    //this will initialize to 0 od

    struct People {
        uint256 fNo;
        string name;
    }

    // people public person = people({fNo:1,name:"vidya"});

    function store(uint256 _f) public{
        f = _f;
    }

    //array syntax is "type of array" "visibilty of array" "name of the array"

    //dynamic array - can change size
    People[] public peopleArr;
    mapping(string => uint256) public nametofNo;

    //view and pure functions are not state changing functions therefore they are blue and not orange

    function retrieve() public view returns(uint256) {
        return f;
    }

    // function retrieve(uint256 f) public pure {
    //     f+f;
    // }

    function addPerson(string memory _fName, uint256 _fNo) public{
        peopleArr.push(People({fNo:_fNo,name : _fName}));
        nametofNo[_fName] = _fNo;
    }

    
}