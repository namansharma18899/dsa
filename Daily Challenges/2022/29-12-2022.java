// Java Program to Demonstrate Working of
// Comparator Interface Via More than One Field

// Importing required classes
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;

// Class 1
// Helper class representing a Student
class Student {

	// Attributes of student
	int start;
    int end;

	// Parameterized constructor
	public Student(Integer start, Integer end)
	{

		// This keyword refers to current instance itself
		this.start = start;
		this.end  = end;
	}
    

	public Integer getStart() {
        return start;
    }

    public void setStart(Integer start) {
        this.start = start;
    }

    public Integer getEnd() {
        return end;
    }

    public void setEnd(Integer end) {
        this.end = end;
    }


    // Class 2
	// Helper class implementing Comparator interface
	static class CustomerSortingComparator
		implements Comparator<Student> {

		// Method 1
		// To compare customers
		@Override
		public int compare(Student customer1,
						Student customer2)
		{

			// Comparing customers
			int StartComp = customer1.getStart().compareTo(customer2.getStart());
            
            int EndCompare= customer1.getEnd().compareTo(customer2.getEnd());
			// 2nd level comparison
			return (EndCompare == 0) ? StartComp
									: EndCompare;
		}
	}

	// Method 2
	// Main driver method
	public static void main(String[] args)
	{

		// Create an empty ArrayList
		// to store Student
		List<Student> al = new ArrayList<>();

		Student obj1 = new Student(1, 3);
		Student obj2 = new Student(2, 6);
		Student obj3 = new Student(3, 5);
		Student obj4 = new Student(4, 5);
		// Student obj5 = new Student(, 29);
		// Student obj6 = new Student(, 22);
		// Adding customer objects to ArrayList
		// using add() method
		al.add(obj1);
		al.add(obj2);
		al.add(obj3);
		al.add(obj4);

		// Iterating using Iterator
		// before Sorting ArrayList
		Iterator<Student> custIterator = al.iterator();

		// Display message
		// System.out.println("Before Sorting:\n");

		// Holds true till there is single element
		// remaining in List
		while (custIterator.hasNext()) {

			// Iterating using next() method
			// System.out.println(custIterator.next());
		}

		// Sorting using sort method of Collections class
		Collections.sort(al,
						new CustomerSortingComparator());

		// Display message only
		// System.out.println("\n\nAfter Sorting:\n");

		// Iterating using enhanced for-loop
		// after Sorting ArrayList
		for (Student customer : al) {
			// System.out.println(customer.start);
		}
	}
}
