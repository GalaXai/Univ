public class Family {
    private Person[] members;

    public Family(Person[] members){
        this.members = members;
    }

    public int adults(){
        int numAdults = 0;

        for(Person member: members){
            if(member.getAge() >= 18){
                numAdults++;
            }
        }
        return numAdults
    }
}
