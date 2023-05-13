import React, { useState } from 'react';
import ReactPaginate from 'react-paginate';
function Paginator(){
  const [currentPage, setCurrentPage] = useState(0);
  const handlePageClick = (data) => {
    const selectedPage = data.selected;
    setCurrentPage(selectedPage);
  };
  return(
    <div>
      {/* 페이지네이션 컴포넌트 */}
      <ReactPaginate
        previousLabel={'이전'}
        nextLabel={'다음'}
        breakLabel={'...'}
        pageCount={10}
        marginPagesDisplayed={2}
        pageRangeDisplayed={5}
        onPageChange={handlePageClick}
        containerClassName={'pagination'}
        activeClassName={'active'}
      />

      {/* 페이지 내용 */}
      <div>
        {/* 현재 페이지에 해당하는 내용 */}
        페이지 {currentPage + 1} 내용
      </div>
    </div>
  );
}

export default Paginator;