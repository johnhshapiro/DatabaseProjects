// Principles of Database Systems
// HWK09
// Author: John Shapiro
// Date: 11.19.2019

// Example MongoDB queries based on prompts from Principles of Database Systems homework

// d) all company names and their number of employees; do not show companies with ‘number_of_employees’ equal to null or zero

db.companies.aggregate(
    [{
            $match: {
                $and: [
                    { 'number_of_employees': { $exists: true } },
                    { 'number_of_employees': { $ne: null } },
                    { 'number_of_employees': { $gte: 1 } }
                ]
            }
        },
        {
            $project: {
                'name': true,
                'number_of_employees': true,
                '_id': false
            }
        }
    ]
)

// e) same as previous but only show the top 10 companies in number of employees; hint: use $sort and $limit.

db.companies.aggregate(
    [{
            $match: {
                $and: [
                    { 'number_of_employees': { $exists: true } },
                    { 'number_of_employees': { $ne: null } },
                    { 'number_of_employees': { $gte: 1 } }
                ]
            }
        },
        {
            $sort: {
                'number_of_employees': -1
            }
        },
        {
            $limit: 10
        },
        {
            $project: {
                'name': true,
                'number_of_employees': true,
                '_id': false
            }
        }
    ]
)

// k) companies by category code, i.e., for each category code, a list of company names in the same category. Hints: the field we are interested in is named ‘category_code’; use the $push operator (slide #12 of lesson 19 has an example). 
db.companies.aggregate(
    [{
            $group: {
                _id: "$category_code",
                "companies": {
                    $push: {
                        "name": "$name"
                    }
                }
            }
        },
        {
            $project: {
                "_id": true,
                "companies": true
            }
        }
    ]
)