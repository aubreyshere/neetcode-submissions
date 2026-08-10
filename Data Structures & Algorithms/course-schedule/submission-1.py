class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        # fill courses with items as prereqs
        for arr in prerequisites:
            if arr[0] not in courses:
                courses[arr[0]] = []
            courses[arr[0]].append(arr[1])

        completable = set()
        visited = set()

        def finishCourse(key: int) -> None:
            if key in completable:
                return True
            elif key in visited:
                return False
            
            visited.add(key)
            if key not in courses:
                print(key)
                completable.add(key)
                return True

            finish = True
            for course in courses[key]:
                finish = finish and finishCourse(course)

            if finish:
                completable.add(key)

            return finish

        for i in range(numCourses):
            finishCourse(i)

        print(completable)
        return len(completable) >= numCourses