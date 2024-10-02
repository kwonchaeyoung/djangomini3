document.addEventListener('DOMContentLoaded', function() {
    // 업종별 게시글 수 데이터 처리 및 차트 생성
    const postsByCuisineData = JSON.parse(document.getElementById('postsByCuisineData').textContent);
    console.log(postsByCuisineData);  // 데이터 확인

    const ctxCuisine = document.getElementById('postsByCuisineChart').getContext('2d');
    const postsByCuisineChart = new Chart(ctxCuisine, {
        type: 'bar',
        data: {
            labels: postsByCuisineData.map(item => item.cuisine),  // 'cuisine' 값을 라벨로 사용
            datasets: [{
                label: '업종별 게시글 수',
                data: postsByCuisineData.map(item => item.count),  // 'count' 값을 데이터로 사용
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // 일자별 게시글 수 데이터 처리 및 차트 생성
    const postsByDayData = JSON.parse(document.getElementById('postsByDayData').textContent);
    console.log(postsByDayData);  // 데이터 확인

    const ctxDay = document.getElementById('postsByDayChart').getContext('2d');
    const postsByDayChart = new Chart(ctxDay, {
        type: 'line',
        data: {
            labels: postsByDayData.map(item => item.day),  // 'day' 값을 라벨로 사용
            datasets: [{
                label: '일자별 게시글 수',
                data: postsByDayData.map(item => item.count),  // 'count' 값을 데이터로 사용
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});

console.log(postsByCuisineData);
console.log(postsByDayData);
