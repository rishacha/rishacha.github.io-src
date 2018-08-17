---
title: Protobuf
# sidebar: auto
# sidebarDepth: 2
---

# Hello Protobuf !

Protobuf is probably the new kid in town. It's new and it's the default format used by Tensorflow framework.


To understand protobuf, it's recommended to understand why we should use protocol buffers. Here's a simple example taken from [here](https://developers.google.com/protocol-buffers/docs/cpptutorial).

### Example : Simple `"address book"`

**Objective** : read/write people's contact details to/from a file. 

**Details**: Each person in the address book has a name, an ID, an email address, and a contact phone number.

**Problem** : How do you serialize and retrieve structured data like this? 

**Solutions** : 
1. The raw in-memory data structures can be sent/saved in binary form. 
    * `Cons` : 
        * Over time, this is a fragile approach, as the receiving/reading code must be compiled with exactly the same memory data in the raw format and copies of software that are wired for that format are spread around, it's very hard to extend the layout, endianness, etc. 
        * Also, as files accumulate data in the raw format and copies of software that are wired for that format are spread around, it's very hard to extend the format
1. You can invent an ad-hoc way to encode the data items into a single string – such as encoding 4 ints as "12:3:-23:67". This is a simple and flexible approach.
    * `Cons` :
        * Requires writing one-off encoding and parsing code
        * The parsing imposes a small run-time cost. This *works best for encoding very simple data*
1. Serialize the data to XML. This approach can be very attractive since XML is (sort of) human readable and there are binding libraries for lots of languages. This can be a good choice if you want to share data with other applications/projects. 
    * `Cons`:
        * However, XML is notoriously space intensive
        * Encoding/decoding it can impose a huge performance penalty on applications
        * Also, navigating an XML DOM tree is considerably more complicated than navigating simple fields in a class normally would be

> Protocol buffers are the flexible, efficient, automated solution to solve exactly this problem. 

### Process
1. With protocol buffers, you write a `.proto` description of the data structure you wish to store. 

    You specify how you want the information you're serializing to be structured by defining protocol buffer message types in `.proto` files.

    ```protbuf
    message Person {
        required string name = 1;
        required int32 id = 2;
        optional string email = 3;

        enum PhoneType {
            MOBILE = 0;
            HOME = 1;
            WORK = 2;
        }

        message PhoneNumber {
            required string number = 1;
            optional PhoneType type = 2 [default = HOME];
        }

        repeated PhoneNumber phone = 4;
    }
    ```

2. From that, the protocol buffer compiler creates a class that implements automatic encoding and parsing of the protocol buffer data with an efficient binary format. 
3. The generated class provides getters and setters for the fields that make up a protocol buffer and takes care of the details of reading and writing the protocol buffer as a unit. 
4. Importantly, the protocol buffer format supports the idea of extending the format over time in such a way that the code can still read data encoded with the old format.


