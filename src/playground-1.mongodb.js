// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("business");


// db.yourCollection.find({}); // Find all documents
// db.yourCollection.insertOne({ name: 'Alice', age: 30 });

// // Switch to the desired database
// use('sampleDB');

// // Insert a sample document into the 'users' collection
// db.users.insertOne({
//     name: 'Alice',
//     age: 30,
//     email: 'alice@example.com',
//     registered: new Date()
// });

// // Find all users older than 25, only return name and email, sorted by age descending
// db.users.find(
//     { age: { $gt: 25 } },           // Filter
//     { name: 1, email: 1, _id: 0 }   // Projection
// ).sort({ age: -1 });              // Sort
