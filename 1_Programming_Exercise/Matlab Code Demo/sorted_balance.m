function [makespan, assigns, accumulators] = sorted_balance(machine_num, job_num, job_indices, job_time)
% *********************************************************************** %
% Sorted Balance Algorithm for Loading Balancing Problem.
% --------
% INPUT  :
% --------
%   machine_num : matrix(1, 1), Integer
%   job_num     : matrix(1, 1), Integer
%   job_indices : matrix(1, job_num), Integer
%   job_time    : matrix(1, job_num), Double
%                 there is an one-to-one mapping relationship between \
%                   *job_indices* and *job_time*
% --------
% OUTPUT :
% --------
%   makespan    : matrix(1, 1), Double
%   assigns     : cell(1, machine_num), Integer
%                 all job indices on each machine [from bottom to top]
%   accumulators: matrix(1, machine_num), Integer
%                 total processing time on each machine
% --------
% Example:
% --------
%   >> [makespan, assigns, accumulators] = sorted_balance(3, 7, 1 : 7, 1 : 7); % 10
%   >> [makespan, assigns, accumulators] = sorted_balance(3, 6, 1 : 6, [2 3 4 6 2 2]); % 7
%   >> [makespan, assigns, accumulators] = sorted_balance(4, 13, [2 : 13 1], [ones(1, 12) 4]); % 4
%   >> [makespan, assigns, accumulators] = sorted_balance(3, 5, 1 : 5, [7 6 5 4 2]); % 9
%   >> job_time = randi(RandStream('mt19937ar', 'Seed', 0), 1e3, 1, 1e3); % job_time(1 , [1 end]) == [815   867]
%   >> [makespan, assigns, accumulators] = sorted_balance(100, 1e3, 1 : 1e3, job_time); % 4906
% *********************************************************************** %
    [job_time, descend_ind] = sort(job_time, 'descend');
    job_indices = job_indices(1, descend_ind);
    [makespan, assigns, accumulators] = greedy_balance(machine_num, job_num, job_indices, job_time);
end
