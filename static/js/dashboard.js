document.addEventListener('DOMContentLoaded', function() {
    // 업종별 게시글 분포 차트
    const postsByCuisineElement = document.getElementById('postsByCuisineData');
    if (postsByCuisineElement) {
        const postsByCuisineData = JSON.parse(postsByCuisineElement.textContent);
        console.log(postsByCuisineData);

        const ctxCuisine = document.getElementById('postsByCuisineChart').getContext('2d');
        const postsByCuisineChart = new Chart(ctxCuisine, {
            type: 'doughnut',
            data: {
                labels: postsByCuisineData.map(item => item.cuisine),  // 'cuisine' 값을 라벨로 사용
                datasets: [{
                    label: '업종별 게시글 수',
                    data: postsByCuisineData.map(item => item.count),  // 'count' 값을 데이터로 사용
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#66CC99', '#CC66FF']
                }]
            }
        });
    }

    // 일자별 게시글 작성 추이 차트
    const postsByDayElement = document.getElementById('postsByDayData');
    if (postsByDayElement) {
        const postsByDayData = JSON.parse(postsByDayElement.textContent);
        console.log(postsByDayData);

        const ctxDay = document.getElementById('postsByDayChart').getContext('2d');
        const postsByDayChart = new Chart(ctxDay, {
            type: 'line',
            data: {
                labels: postsByDayData.map(item => item.day),  // 'day' 값을 라벨로 사용
                datasets: [{
                    label: '일자별 게시글 수',
                    data: postsByDayData.map(item => item.count),
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            }
        });
    }
});
